import numpy as np

p_h1 = 0.5
p_h2 = 0.5

def likelihood(data,hypothesis):
    if hypothesis == "h1":
        return 0.5
    elif hypothesis == "h2":
        if data == "H":
            return 0.7
        else:
            return 0.3


            ##return 0.7 if data=="h" else 0.3  ####use this much more neat


def bayesian_update(prior_h1,prior_h2,data):

    likelihood_h1 = likelihood(data, "h1")
    likelihood_h2 = likelihood(data, "h2")

    #print(likelihood_h1, prior_h1)
    P_data = likelihood_h1 * prior_h1 + likelihood_h2 * prior_h2

    posterior_h1 = (likelihood_h1 * prior_h1)/P_data

    posterior_h2 = (likelihood_h2 * prior_h2)/P_data

    return posterior_h1, posterior_h2

coin_flips =np.random.choice([1,0],size=20)

#print(coin_flips)

p_h1_posterior = p_h1
p_h2_posterior = p_h2

##flips is our data

for flip in coin_flips:
    p_h1_posterior,p_h2_posterior = bayesian_update(p_h1_posterior,p_h2_posterior,flip)

    print(f" flip {flip}:p(h1|data) = {p_h1_posterior:.4f} ,{p_h2_posterior:.4f}")
