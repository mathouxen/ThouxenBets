# Thouxen Bets ⚽

A Python-based football match prediction project that uses historical match data to predict the **directional outcome** of future football matches:

- 🏠 Home win
- 🤝 Draw
- ✈️ Away win

The project starts with a simple, interpretable approach rather than immediately using complex machine-learning models. The goal is to build the predictor incrementally, test each improvement, and measure whether it actually improves prediction accuracy.

---

## 🎯 Project Goal

The current goal of Thouxen Bets is **directional accuracy**.

The MVP asks:

> Given the information available before a match, can we correctly predict whether the home team will win, the match will be a draw, or the away team will win?

The project is **not currently focused on**:

- Exact score prediction
- Betting odds
- Stake sizing
- Betting strategies
- Maximising financial returns

Those may become future areas of exploration, but the current focus is simply building and evaluating a football outcome predictor.

---

## 🧠 How the MVP Works

The current predictor uses several basic indicators of team performance.

### 1. Recent Form

The model looks at a team's recent matches and records each result as:

```text
W = Win
D = Draw
L = Loss
```

Form is converted into points:

```text
Win  = 3 points
Draw = 1 point
Loss = 0 points
```

For example:

```text
W W D L W
```

produces:

```text
3 + 3 + 1 + 0 + 3 = 10 points
```

---

### 2. Goals Scored

The model records the number of goals a team scored in its recent matches.

This provides a simple measure of attacking performance.

---

### 3. Goals Conceded

The model also records the number of goals a team conceded in its recent matches.

This provides a simple measure of defensive performance.

---

### 4. Team Strength

The recent form, goals scored and goals conceded are combined into a basic team-strength value.

The two teams are then compared:

```text
delta = home_strength - away_strength
```

The current prediction logic is:

```text
delta > 0  → Home win
delta < 0  → Away win
delta = 0  → Draw
```

This gives the MVP a simple and interpretable prediction mechanism.

---

## ⏱️ Time-Aware Predictions

A key requirement of the project is that the model must not use information from the future.

When predicting a match, the model should only use matches that occurred **before the match being predicted**.

For example:

```text
Match 1
Match 2
Match 3
...
Match 19
Match 20 ← prediction
Match 21
...
```

When predicting Match 20, the model can use Matches 1–19, but must not use Matches 21 onward.

The `stats()` function therefore works backwards from the current match index to collect historical information.

This prevents **data leakage** and makes the evaluation more representative of how the model would behave in practice.

---

## 📊 Data Format

The current dataset is stored chronologically.

Relevant row indexes are:

|    Index | Data         |
| -------: | ------------ |
| `row[3]` | Home team    |
| `row[4]` | Away team    |
| `row[5]` | Home goals   |
| `row[6]` | Away goals   |
| `row[7]` | Match result |

The result is represented as:

```text
H = Home win
D = Draw
A = Away win
```

The project currently uses Python and CSV-based football data.

---

## 🧩 Current Core Functions

### `stats(home, away, indexed)`

Collects historical statistics for both teams before the match at `indexed`.

It currently gathers:

- Goals scored
- Goals conceded
- Recent form

The function works backwards through previous matches and is the **time-aware version used by the MVP**.

---

### `stats2(...)`

Processes the collected goal data and calculates averages.

It also handles cases where a team has insufficient historical data.

---

### `form_score(home_recent_form, away_recent_form)`

Converts recent form into numerical points:

```text
Win  → 3
Draw → 1
Loss → 0
```

---

### `teamStrength2(...)`

Combines the team's recent form and goal statistics to produce:

```text
home_strength
away_strength
delta
```

The delta is then used by the prediction logic.

---

## 🧪 Evaluation

The MVP evaluates predictions against the actual match result.

The current evaluation is intentionally strict.

A prediction is considered correct when:

```text
delta > 0  AND actual result = H
```

or:

```text
delta < 0  AND actual result = A
```

or:

```text
delta == 0 AND actual result = D
```

A draw is therefore only predicted when the two calculated strengths are exactly equal.

This is an area that may be improved later.

---

## 🔍 Current Findings

Testing the basic team-strength model revealed an interesting pattern.

A significant proportion of incorrect predictions were:

> The home team won, while the model favoured the away team.

This suggests that the current model may be missing an important factor:

### Home-ground advantage

The project will eventually investigate whether incorporating an empirically measured home advantage improves prediction accuracy.

The important principle is that this will be **tested rather than assumed**.

---

## 🛠️ Current Development Status

The project recently underwent a major code restructuring.

The original MVP was becoming difficult to read and reuse because too much functionality was concentrated in the same areas.

The code has therefore been reorganised into smaller functions with clearer responsibilities.

### Current status

- ✅ Core MVP implemented
- ✅ Historical statistics collection
- ✅ Time-aware statistics
- ✅ Recent-form calculation
- ✅ Goal statistics
- ✅ Basic team-strength calculation
- ✅ Prediction evaluation
- ✅ Major code restructuring
- 🔧 Minor refactoring still remaining
- ⏳ Home-advantage investigation
- ⏳ Improved draw handling
- ⏳ Further model evaluation

---

## 🗺️ Future Development

The project is intended to evolve incrementally.

Potential improvements include:

### Home Advantage

Calculate an empirical home advantage from historical results and determine whether adding it improves predictions.

### Better Draw Handling

The current system only predicts a draw when:

```text
delta == 0
```

A future version could use a more flexible method for estimating draw probability.

### Home/Away Performance

Instead of treating all recent matches equally, the model could investigate:

- Home team's home performance
- Away team's away performance
- How strongly venue affects each team

### Improved Team Strength

Additional factors can eventually be introduced if testing shows that they provide useful predictive information.

### More Advanced Models

Once the simple MVP has been properly evaluated, the project could experiment with statistical or machine-learning approaches.

The simple model provides a useful baseline against which more complicated models can be compared.

---

## 📁 Project Philosophy

Thouxen Bets follows a simple development philosophy:

> **Start simple → measure → identify weaknesses → improve → measure again.**

The intention is not to build a complicated model immediately.

Instead, each new feature should answer a question:

1. What weakness does this feature address?
2. Can we measure the feature using historical data?
3. Does adding it improve prediction performance?
4. Is the improvement worth the additional complexity?

This keeps the project understandable and makes it easier to determine which parts of the model actually contribute value.

---

## 🚀 Long-Term Vision

The long-term goal is to develop Thouxen Bets from a simple rule-based MVP into a more capable football prediction system while maintaining a strong emphasis on:

- Clean and reusable code
- Time-aware data
- Reliable evaluation
- Measurable improvements
- Understanding why the model makes its predictions

The MVP is the foundation for that process.

---

## ⚠️ Disclaimer

Thouxen Bets is a software and data-analysis project for experimentation and learning.

Football predictions are inherently uncertain, and historical performance does not guarantee future results.
