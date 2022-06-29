# ss22-pqc-code-based-challenge
Post-Quantum Cryptography Code Based Challenge for summer semester 2022

The goal of this lecture is, to understand state-of-the-art pqc algorithms and implement a toy example.

In this repo, a (small) solution for the *syndrome decoding problem* for code-based cryptography is given.
The challenge is proposed at [decodingchallenge.org](https://decodingchallenge.org/syndrome)

## Milestones

* [ ] understand decryption and encryption in McEliece Algorithm
* [ ] implement McEliece in Python
    * [ ] public key, secrect key generation
    * [ ] generation of cipher $c = H*m + e$
* [ ] find an $e$ by **brute-force**
* [ ] increase security parameters until time threshold for brute force is too big
* [ ] understand Prange's algorithm
* [ ] Compute a valid $e$ by Prange's algorithm
* [ ] Time comparison (complexity comparison) of both methods

## The Challenge

**Syndrome Decoding problem.** Given integers *n,k,w* such that $k \le n$ and $w \le n$, an instance of the problem SD(*n,k,w*) consists of a parity-check matrix $$H \in F^{(n−k)×n}_2$$ and a vector $$s \in F^{(n−k)}_2$$ (called the syndrome). A solution to the problem is a vector $$e \in F^n_2$$ of Hamming weight $\le w$ such that $$He^⊤=s^⊤$$

**The challenge.** Here, we focus on instances with code rate $R=0.5$, that is $n=2k$. We will choose a weight $w$ slightly higher than the **Gilbert-Varshamov** bound: $$w=\lceil 1.05dGV \rceil$$ The matrix **H** and the syndrome **s** are picked uniformly at random. In this context, with very high probability there exists a vector $e$ of weight $(\le w)$ such that $$He^⊤=s^⊤$$

Under these conditions, instances with cryptographic size are assumed to be out of reach, so we propose instances with increasing size to see how hard this problem is in practice. The Low-weight Codeword challenge proposes another approach: instances of fixed cryptographic size but where the goal is to make $w$ as small as possible. 
