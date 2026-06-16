# THE LANGUAGE OF THE MACHINE · LMC

A UD0 (Artificial Intelligence domain) sphere built **off** Anthropic's **HH-RLHF**
human-preference dataset — the `{chosen, rejected}` pairs behind RLHF.

**The thesis:** the *delta* between the chosen and the rejected response is the
measure — the human judgment that becomes the **gate** (the reward model RLHF
optimizes against). A language taught by preference, not by rule. Woven with
**LIMEN** (the boundary-crossing human/machine tongue, from the PULSE sphere) and
**THE AMBASSADOR** (its speaker).

→ **Live:** https://davidwise01.github.io/language-of-the-machine/

## Two layers, kept honest

- **The DATA is Anthropic's**, cited — *not* claimed as ROOT0's:
  - Paper: Bai et al., *"Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback"* (2022) — [arXiv:2204.05862](https://arxiv.org/abs/2204.05862)
  - Red-team paper: *"Red Teaming Language Models to Reduce Harms"* — [arXiv:2209.07858](https://arxiv.org/abs/2209.07858)
  - Canonical dataset (MIT): https://huggingface.co/datasets/Anthropic/hh-rlhf
- **The FRAMING is ROOT0's** — preference as "the language of the machine," the delta as the gate, LIMEN, the Ambassador.

## What's here / not here

- This repo ships the **page, counts, structure, and one benign example** — **not** the data files.
- **No harmful content is republished.** Per the dataset's own disclaimer the corpus
  contains offensive material; the companion **red-team** transcripts are deliberately
  **excluded** and left at the canonical source for harm-reduction research only.

## The counts (file-verified, the packaged preference subset)

| Tranche | train | test |
|---|--:|--:|
| helpful-base | 43,835 | 2,354 |
| helpful-rejection-sampled | 52,421 | 2,749 |
| helpful-online | 22,007 | 1,137 |
| harmless-base | 42,537 | 2,312 |
| **TOTAL** | | **169,352 pairs** |

## Load the real data (from the source)

```python
from datasets import load_dataset
ds = load_dataset("Anthropic/hh-rlhf")                 # all helpful + harmless
# red-team (separate, harm-reduction research only):
# load_dataset("Anthropic/hh-rlhf", data_dir="red-team-attempts")
```

Each preference line: `{"chosen": "<Human/Assistant transcript>", "rejected": "<transcript>"}`.

---

*Framing © David Lee Wise / ROOT0 · TriPod LLC · CC-BY-ND-4.0 · TRIPOD-IP-v1.1. Data © Anthropic, MIT, for harm-reduction research. Catalogued into UD0; connects to PULSE·LIMEN and ALIGNMENT.*
