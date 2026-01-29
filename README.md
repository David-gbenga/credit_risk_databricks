PROJECT OVERVIEW
Credit Risk Prediction Platform — Tech Reyal Ltd
Tech Reyal Ltd is building a production-ready Credit Risk Prediction Application for fintechs, lenders, credit unions, and BNPL providers to make faster, safer, and more consistent lending decisions. The platform combines probability-of-default modelling, scorecard-style risk bands, policy decisioning, and model explainability to deliver underwriting outcomes that are interpretable, auditable, and operationally usable.
At its core, the solution takes applicant/account data (e.g., affordability, credit behaviour, utilisation, repayment performance, exposure attributes) and produces a compact set of decision outputs for both individual decisions and portfolio-level risk management. The design is modular, allowing institutions to plug in their own data sources, policies, and risk appetite while maintaining transparent governance for model risk and regulatory compliance.

What the Platform Produces Per Applicant / Account
1) Probability of Default (PD)
The model estimates the likelihood that an applicant will default within a defined horizon (e.g., 12 months).
Example output: PD = 3.2%
Used for: approve/decline decisions, risk-based pricing, credit limit setting, and portfolio risk estimation.
2) Risk Score / Scorecard Band
Applicants are mapped to an easily interpretable score or banding system.
Example output: Score = 620 or Band = A–E
Used for: consistent underwriting, segmentation, and policy rules (e.g., minimum band thresholds per product).
3) Decision Recommendation (Approve / Refer / Decline)
A policy engine combines PD and risk bands with affordability and business rules to recommend an action.
Example output: Decision = Refer
Used for: reducing manual review workload, improving speed and consistency, and ensuring standardised decisioning across channels.
4) Expected Loss (EL) and related metrics
The platform computes risk metrics aligned to credit risk frameworks such as IFRS 9:
EL = PD × LGD × EAD (optionally supporting scenario-based stress adjustments).
Used for: provisioning, capital planning, and portfolio strategy.
5) Pricing Inputs (Risk-based pricing)
The service generates pricing guidance from PD/EL, such as a risk premium or recommended APR range.
Example output: Recommended APR uplift = +2.1%
Used for: balancing growth and profitability, reducing adverse selection, and maintaining competitive pricing.
6) Early Warning Signals / Monitoring Flags
For existing accounts, the system identifies deterioration trends and triggers watchlist flags.
Example outputs: “Risk rising”, “Payment stress”, “Utilisation spike”
Used for: proactive collections, targeted customer support, and loss prevention.
7) Explainability / Reason Codes
Each prediction and decision is accompanied by interpretable “reason codes” describing key drivers.
Example outputs: “High utilisation”, “Thin credit file”, “Recent missed payments”
Used for: transparency, regulatory compliance, customer communication, and appeals handling.
8) Portfolio Insights & Stress Testing
Beyond single decisions, the platform aggregates results to show risk concentration and scenario projections.
Example outputs: risk distribution by segment, projected defaults under adverse scenarios, changes in EL under stress.
Used for: risk appetite setting, downturn planning, and strategic portfolio adjustments.

How It Works (Workflow)
1.	Data ingestion & validation: Accept applicant/account data via batch (CSV/DB) or API; enforce schema checks and data quality rules.
2.	Feature engineering: Build predictive features (behavioural, affordability, utilisation, credit history, exposure).
3.	Model scoring: Generate PD using a calibrated model; map outputs to score/band.
4.	Decisioning: Apply institution rules (policy thresholds, affordability constraints, product rules) to recommend approve/refer/decline.
5.	Risk metrics: Compute EL (and related measures) for provisioning and portfolio reporting.
6.	Explainability: Produce reason codes and local explanations for each applicant.
7.	Monitoring: For booked accounts, track PD drift and early warning triggers over time.
8.	Portfolio analytics: Summarise results across segments and run scenario-based stress tests.

Intended Users
•	Underwriting & Credit Risk Teams: fast decisions with transparent reasons
•	Pricing & Growth Teams: risk-adjusted pricing and profitability control
•	Collections Teams: early warning signals for intervention
•	Risk Governance / Compliance: explainability, audit trails, consistent policy application
•	Product & Analytics Teams: portfolio insights to support strategy
