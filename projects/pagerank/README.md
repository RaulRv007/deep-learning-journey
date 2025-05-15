
# PageRank Algorithm

This Python project implements the **PageRank algorithm**, a key component behind search engines like Google. It estimates the importance of web pages based on the structure of links between them. This implementation supports both **sampling-based** and **iterative** approaches.

## 📂 Project Structure

- `pagerank.py`: Main program to compute PageRank values.
- Input: A folder containing `.html` files, each with links to other pages.
- Output: Estimated PageRank values for each page in the corpus.

## 🚀 How It Works

### 1. **Crawl**
Parses a directory of `.html` files and builds a **link graph** where each page maps to the set of other pages it links to (within the same corpus).

### 2. **Transition Model**
Defines the probability of moving from one page to another based on:
- Damping factor (e.g., 85% chance to follow a link, 15% random jump).
- The structure of outbound links.

### 3. **Sampling Method**
Simulates a random surfer by:
- Starting at a random page.
- Choosing the next page based on the transition model.
- Repeating this process for `n` samples.
- Estimating PageRank by relative frequency.

### 4. **Iterative Method**
Starts with equal rank for each page and updates ranks iteratively using the PageRank formula until the values converge (change < 0.001).

## 🧪 Usage

```bash
python pagerank.py corpus/
```

- `corpus/` should be a directory containing HTML files with hyperlinks between them.

## 📊 Sample Output

```
PageRank Results from Sampling (n = 10000)
  1.html: 0.2154
  2.html: 0.3420
  3.html: 0.4426
PageRank Results from Iteration
  1.html: 0.2170
  2.html: 0.3395
  3.html: 0.4435
```

## ⚙️ Configuration

- **Damping Factor**: Set to 0.85 by default.
- **Samples**: Number of samples (default: 10000) for the sampling approach.

You can tweak these values in the `pagerank.py` file:

```python
DAMPING = 0.85
SAMPLES = 10000
```

## 🧠 Concepts Covered

- Markov Chains
- Random Walks
- Probabilistic Modeling
- Iterative Approximation
- HTML Parsing

## 📚 References

- [Google's original PageRank paper](https://en.wikipedia.org/wiki/PageRank)
- CS50 AI Course — Project: PageRank

---

## 🛠️ To-Do

- [ ] Improve iteration logic to consider all inbound links.
- [ ] Add visualization of the link graph.
- [ ] Add unit tests for core functions.
- [ ] Convert to a Python package.

## 📜 License

This project is licensed under the MIT License.
