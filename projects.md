---
layout: page
title: Projects
permalink: projects
---

## Building Endangered Language Technology (BELT)

[BELT](https://belt.rc.colorado.edu) is a highly-interactive course for creating low-resource language technology with no prior programming experience. The goal of BELT is to make it easy to build and deploy usable, real-world tools for speakers within endangered language communities. BELT is available as an online platform and occasionally an in-person workshop, the most recent of which was January 2024 in Santiago, Chile.

## Interlinear Gloss Generation

Interlinear Glossed Text (IGT) is a common format used by linguists for language documentation, and it can be used to accelerate the development of low-resource NLP approaches. Since the creation of IGT is time-consuming and painstaking, there is great benefit to partially automating the process. I've researched various neural approaches to automating IGT creation, exploring techniques such as transfer learning, multistage denoising, and semi-supervised training.

For the [GenBench workshop](https://genbench.org/workshop/) on generalization, I [researched](https://aclanthology.org/2023.genbench-1.7/) the robustness of IGT models, finding significant challenges with domain transfer. I studied techniques to improve this issue, finding particular success with semi-self-supervised learning in the form of iterative pseudolabeling.

In the [GlossLM](https://arxiv.org/abs/2403.06399) project, I collected a huge multilingual corpus of IGT and pretrained models on it. I have also studied whether in-context learning with LLMs can be effective for glossing.

## PyFoma

With my advisor Prof. Mans Hulden, I have contributed to the development of [PyFoma](https://github.com/mhulden/pyfoma), a toolkit for the development of finite-state technology. In particular, I helped refactor the package to use a consistent Python API, deployed the package to package managers such as PyPI and Anaconda, and created features including drawing context-free grammar trees.
