# Lab Manual 2 Report
Course: CSE-478 Introduction to Computer Security

---

# CheckPoint 1: Breaking Caesar Cipher

## Objective
To break a Caesar cipher using brute-force attack and demonstrate its weakness.

## Given Cipher
odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo

## Approach

The Caesar cipher shifts each letter by a fixed number of positions.

Since the English alphabet has 26 letters, there are only 25 possible keys (excluding shift 0).

To break the cipher:

1. I implemented a brute-force program in C++.
2. The program tried all 25 possible shifts.
3. For each shift, the program printed the decrypted result.
4. I manually inspected the outputs to find meaningful English text.

## Result

At shift 10, the correct plaintext was obtained:

ethereumisthebestsmartcontractplatformoutthere

This confirms that the encryption key used was 10.

## Why Caesar Cipher is Weak

- Very small key space (only 25 keys).
- Can be broken instantly using brute force.
- No resistance against computational attacks.
- Does not hide letter frequency patterns.

Conclusion:
Caesar cipher is completely insecure in modern cryptography.

---

# CheckPoint 2: Breaking Substitution Cipher

## Objective
To break two monoalphabetic substitution ciphers using frequency analysis and pattern recognition.

## What is Substitution Cipher?

A substitution cipher replaces each plaintext letter with another unique letter.

Unlike Caesar cipher, the shift is not fixed.
There are 26! possible keys, which makes brute force impractical.

However, substitution ciphers are still weak because they preserve frequency patterns.

---

## Approach Used

### Step 1: Frequency Analysis

I wrote a C++ program to:

- Read cipher text from file
- Count frequency of each letter
- Sort letters by highest frequency

English language has known frequency distribution:

E ≈ 12%
T ≈ 9%
A ≈ 8%
O ≈ 7%
I ≈ 6%
N ≈ 6%

The most frequent letter in ciphertext likely corresponds to 'E'.

---

### Step 2: Pattern Recognition

After observing frequency output:

- Looked for repeated 3-letter words
- For example: a repeated word like "cei"
- Likely mapping: "the"

So:
c → t  
e → h  
i → e  

Then gradually replaced letters manually.

---

### Step 3: Iterative Replacement

By replacing guessed letters:

- Words started forming
- Context became clearer
- More mappings were discovered

This process continued until readable English text appeared.

---

## Which Cipher Was Easier?

Cipher 2 was easier because:

- It was longer.
- Frequency distribution was more stable.
- Word patterns were clearer.
- More statistical information available.

Cipher 1 was harder because:

- Shorter text.
- Less frequency stability.
- Required more guessing.

---

# Why Substitution Cipher is Weak

Even though there are 26! possible keys:

- It preserves letter frequency.
- Common words like "the", "and", "is" appear repeatedly.
- Statistical attacks can break it.

Thus, monoalphabetic substitution ciphers are insecure.

---

# Final Conclusion

Both Caesar and Substitution ciphers are vulnerable because:

- They do not hide statistical properties of language.
- They have predictable structure.
- They can be broken using computational and analytical methods.

This lab demonstrates why classical cryptography is no longer secure in modern systems.
