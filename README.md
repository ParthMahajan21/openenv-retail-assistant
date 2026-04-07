---
title: OpenEnv Retail Assistant
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
---

# 🧠 OpenEnv Retail Assistant

An OpenEnv-compliant AI environment that simulates real-world retail tasks such as email triage, customer support, and data analysis with automated evaluation.

---

## 🌐 Live Demo

👉 https://huggingface.co/spaces/ParthMahajan21/openenv-retail-assistant

---

## 🧩 Problem Statement

Most AI systems today are tested using simple benchmarks or toy problems that don’t reflect how tasks work in the real world. Because of this, an AI model might perform well in testing but struggle when applied to practical situations.

In reality, people use AI for tasks like responding to customer queries, sorting emails, or analyzing messy data. However, there isn’t a structured and standardized way to test how well AI performs in these real-world scenarios.

This creates a gap between theoretical performance and actual usefulness.

To solve this, we need an environment where AI agents can:
- Work on realistic, everyday tasks  
- Receive clear inputs and produce meaningful outputs  
- Be evaluated using consistent and fair scoring methods  
- Get feedback that reflects their progress  

This project builds such an environment using OpenEnv, focusing on retail-based tasks.

---

## 🚀 Overview

OpenEnv Retail Assistant is designed to evaluate AI agents in realistic retail scenarios.

It includes:
- Real-world task simulation
- Automated grading system
- Interactive UI
- Containerized deployment

---

## 🧪 Tasks

### 🟢 Easy — Email Classification
Classify customer intent (e.g., refund request)

### 🟡 Medium — Customer Support
Generate polite and helpful responses

### 🔴 Hard — Data Analysis
Clean messy data and provide insights

---

## 🎯 Reward Function

The environment provides a continuous score between **0.0 and 1.0**:

- **1.0** → Fully correct response  
- **0.5** → Partially correct  
- **0.0** → Incorrect response  

This ensures meaningful feedback instead of binary evaluation.

---

## ⚙️ OpenEnv Compliance

This project follows OpenEnv specifications:

- Typed Observation, Action models using Pydantic  
- `reset()` → initializes environment  
- `step(action)` → returns observation, reward, done, info  
- `state()` → returns current state  
- Deterministic grading system  

---

## 📊 Baseline Results

| Task   | Score |
|--------|------|
| Easy   | 1.0  |
| Medium | 1.0  |
| Hard   | 1.0  |

---

## 🖥️ Features

- Interactive UI (Gradio)
- Real-time scoring
- Gradient-based modern interface
- Multi-task simulation
- Fully containerized (Docker)

---

## 🐳 Deployment

This project is deployed using:

- Docker
- Hugging Face Spaces

---

## 📂 Project Structure
