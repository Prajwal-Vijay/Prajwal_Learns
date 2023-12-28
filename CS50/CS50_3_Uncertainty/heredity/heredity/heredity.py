import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")
    people = load_data(sys.argv[1])

    # Keep track of gene and trait probabilities for each person
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    #Storing the Gene Count
    data = {
                person: {
                    "probability":1,
                    "geneCount":None
                }
                for person in people
            }
    for person in data:
        if person in one_gene:
            data[person]["geneCount"] = 1
        elif person in two_genes:
            data[person]["geneCount"] = 2
        else:
            data[person]["geneCount"] = 0
    
    #Assigning Probabilities Begins Here
    for person in people:
        m = people[person]["mother"]
        f = people[person]["father"]
        s = [m,f]

        #If the Person has no Parent then simply assign prob. and move on.
        if m is None:
            data[person]["probability"] *= PROBS["gene"][data[person]["geneCount"]]
            if person in have_trait:
                data[person]["probability"] *= (PROBS["trait"][data[person]["geneCount"]][True])
            else:
                data[person]["probability"] *= (PROBS["trait"][data[person]["geneCount"]][False])
            continue
        
        #For Person With GeneCount = 0
        if data[person]["geneCount"] == 0:
            for i in s:
                g = data[i]["geneCount"]
                if g == 0:
                    data[person]["probability"] *= (1-PROBS["mutation"])
                elif g == 1:
                    data[person]["probability"] *= 0.5
                else:
                    data[person]["probability"] *= (PROBS["mutation"])
                
            
        #For person with gene count = 1
        elif data[person]["geneCount"] == 1:
            gm = data[m]["geneCount"]
            gf = data[f]["geneCount"]
            po = 1 #Probability Offspring
            if gm == 0 and gf == 0:
                po *= (1-PROBS["mutation"])*PROBS["mutation"]*2
            elif (gm == 1 and gf == 0) or (gm == 0 and gf == 1):
                po *= 0.5
            elif (gm == 1 and gf == 1):
                po *= 0.25
            elif (gm == 2 and gf == 1) or (gm == 1 and gf == 2):
                po *= 0.5
            elif (gm == 2 and gf == 0) or (gf == 0 and gm == 2):
                po *= ((1-PROBS["mutation"])**2 + (PROBS["mutation"])**2)
            elif (gm == 2 and gf == 2):
                po *= (1-PROBS["mutation"])*PROBS["mutation"]*2
            #Donot Forget this!
            data[person]["probability"]*=po
            
        #For person with gene count = 2
        else:
             for i in s:
                g = data[i]["geneCount"]
                if g == 0:
                    data[person]["probability"] *= (PROBS["mutation"])
                elif g == 1:
                    data[person]["probability"] *= 0.5
                else:
                    data[person]["probability"] *= (1-PROBS["mutation"])
            
            
        #Multiplying the trait
        if person in have_trait:
            data[person]["probability"] *= (PROBS["trait"][data[person]["geneCount"]][True])
        else:
            data[person]["probability"] *= (PROBS["trait"][data[person]["geneCount"]][False])
    final_prob = 1
    for j in data:
        final_prob *= data[j]["probability"]
        
    return final_prob

        
def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    for person in one_gene:
        probabilities[person]["gene"][1] += p
    for person in two_genes:
        probabilities[person]["gene"][2] += p
    for person in (set(probabilities.keys()) - set(one_gene) - set(two_genes)):
        probabilities[person]["gene"][0] += p
    for person in have_trait:
        probabilities[person]["trait"][True] += p
    for person in (set(probabilities.keys()) - set(have_trait)):
        probabilities[person]["trait"][False] += p

def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    for person in probabilities:
        s = probabilities[person]["gene"][0] + probabilities[person]["gene"][1] + probabilities[person]["gene"][2]
        if s >0 :
            probabilities[person]["gene"][0] /= s
            probabilities[person]["gene"][1] /= s
            probabilities[person]["gene"][2] /= s
            
        s = probabilities[person]["trait"][True] + probabilities[person]["trait"][False]
        if s >0 :
            probabilities[person]["trait"][True] /= s
            probabilities[person]["trait"][False] /= s
        
if __name__ == "__main__":
    main()
