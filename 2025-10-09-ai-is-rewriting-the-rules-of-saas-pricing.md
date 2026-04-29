# Rubik's Cube

*The end of seats, the rise of outcomes.*


**Published:** 2025-10-09  
**Source:** [https://bmak.substack.com/p/the-era-of-ai-pricing-extended](https://bmak.substack.com/p/the-era-of-ai-pricing-extended)

---

For years, SaaS pricing was based on a simple pricing model: price per seat. Easy to explain, easy to forecast, and easy to sell. But that model is breaking down. As AI reshapes workflows and automation reduces the need for “seats”, the link between user count and value delivered is eroding.

## **This is Not the First Shift**

SaaS pricing has evolved before. In the early 2000s, the industry shifted from one-off license purchases to subscriptions. Back then, you could buy software on a CD-ROM and pay a one-time fee. As internet speeds increased and agile development enabled continuous updates, companies moved to subscription models charging monthly or annually for access instead of ownership.

This evolved further into seat-based pricing, where customers paid based on the number of users, and then into tiered models that segmented users by capabilities, storage, or support. Each evolution reflected a change in how customers used software and how vendors delivered value.

[](https://substackcdn.com/image/fetch/$s_!u0bb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F929f6506-c6e8-4b17-a711-4f5eb11caf4c_1024x1024.png)

## **Why the Shift?**

The subscription seat-based model works in a world where value scales with headcount. More employees means more licenses, and more licenses means more revenue. But AI changes this equation.

One AI agent can amplify or replace the work of many humans and one human can deploy many agents. Instead of growth in seats, companies are seeing flat or even declining user counts, while actual usage of the system skyrockets. This shift breaks the seat metric as a proxy for value.

At the same time, most AI products fall in the base model wrapper category. This isn’t a criticism as many successful SaaS products are database wrappers but it does change the cost structure. Traditional SaaS products have minimal marginal costs per use to the vendor mostly in the form of compute, storage, and memory as most software products are offered as managed solutions. Heavy Slack users don’t dramatically increase Slack’s infrastructure costs. But with AI, high usage directly drives marginal costs, as each prompt consumes tokens. Vendors need pricing models that protect margins as usage scales.

Thanks for reading Rubik's Cube! Subscribe for free to receive new posts and support my work.

Subscribe

## **How to Price**

The most helpful framework I have found (not surprisingly) comes from Madhavan Ramanujam. The [model](https://www.emcap.com/thoughts/charging-for-intelligence-how-to-price-ai-software?) is based on a 2x2 matrix with autonomy (level of independence of the AI product) and attribution (how close can my product link to a business outcome) on the two sides. This is helpful not only for how to price right now, but also for how to think strategically of where you want to be and define the right product strategy. Each product falls in one of four quadrants:

**1. Low Autonomy + Low Attribution (Seat based pricing)**

Companies in this quadrant typically charge by seat, as AI feature outcomes are hard to measure precisely. AI capabilities can become a plan differentiator so vendors can segment users to different tiers. For example, [Notion](https://www.notion.com/pricing) is charging by seat and uses AI features as a way to segment users. If a user finds value in Notion AI features, they have to select the Business or Enterprise plans (and pay at least ten euros more per seat/ month for this access). Tomasz Tunguz [analyzed](https://tomtunguz.com/ai-copilot-premium-pricing/) this strategy and found that offering AI capabilities as part of your product increases the price by a range between 30-110%.

[](https://substackcdn.com/image/fetch/$s_!0OgI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00b3930e-1608-4ebf-9a83-5b969895b662_1272x772.png)

To protect margins, companies often introduce rate limits for heavy users. [Fireflies AI](https://fireflies.ai/pricing) applies a rate [limit](https://guide.fireflies.ai/articles/2631950139-learn-about-transcription-credits-storage-and-rate-limits-for-meetings) of 3,000 mins/source/month with any overage charged at $0.01/min.

[](https://substackcdn.com/image/fetch/$s_!vlHW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8491b238-7ca8-4a6d-bd35-01722faddc4a_1106x752.png)

If you extend this rate limits logic, products can evolve to usage based pricing and get to the next quadrant.

**2. Low Autonomy + High Attribution (Hybrid pricing)**

A natural next step is hybrid pricing, maintaining seats while adding a usage component (tokens, credits, or calls). As seat counts flatten, consumption increases. Vendors can monetize usage by bundling token allotments into plans, encouraging upgrades, or selling extra credits.

For example, [Lovable](https://lovable.dev/pricing) uses a hybrid model. Its Pro tier includes 100 credits for $25/month, but users can purchase up to 10,000 credits for $2,250/month, a near 100x increase in both usage and revenue. This model preserves simplicity while capturing upside from heavy users.

[](https://substackcdn.com/image/fetch/$s_!Vf4o!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F532c92a5-400f-42ea-9d90-909b47816dc5_907x719.png)

**3. High Autonomy + Low Attribution (Pricing Utilities)**

The other option, better suited for infrastructure providers is usage based pricing, at times combined with a base price. The main assumption is that token usage is a good proxy for value. It can work well at the platform level since a base model supports many different use cases. Companies are used to paying for cloud resources as a utility. For example, Amazon EC2 is [charging](https://aws.amazon.com/ec2/pricing/on-demand/) for instances by the hour. Given it is very hard for EC2 to segment based on the profitability of each application, the assumption that the more compute you are using the more value you get is a decent one and the same applies to ChatGPT [tokens](https://openai.com/api/pricing/).

Note that this model creates a variable cost for customers. To minimize unpleasant surprises, vendors invest resources on customer facing dashboards and APIs to inform them about usage and cost during the billing period, while also developing tooling to help them optimize (e.g., recommend a cheaper product if the value/cost ratio is worth it). AWS is quite [sophisticated](https://aws.amazon.com/aws-cost-management/cost-optimization/) in this domain and I assume OpenAI and others are already developing similar infrastructure.

[](https://substackcdn.com/image/fetch/$s_!12Z-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F18c19d29-92c9-4f32-aa6e-109b114f2914_1174x372.png)

[](https://substackcdn.com/image/fetch/$s_!brft!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff2afe0c3-aaf3-4a0c-a7c4-54e8321daebf_1181x449.png)

**4. High Autonomy + High Attribution (Getting closer to value)**

While the assumption that token usage is a good proxy for value is acceptable for utilities, it can be challenging for other applications. For example, imagine two customer support AI agents that are resolving the same number of cases but one of them is messaging customers twice as much and therefore using twice the tokens. In this case, the token consumption is not a good proxy of value. On the contrary, messaging customers more times to resolve an issue might create negative experiences, while a pricing model that charges based on token usage is providing wrong incentives to the vendor. For higher-in-the-stack applications that can tie their value to specific business outcomes, usage based is being replaced by charging for an action or outcome. For example, Zendesk is [charging](https://www.zendesk.com/pricing/) $1.50-2 per automated resolution.

[](https://substackcdn.com/image/fetch/$s_!y9Hl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe7e6261b-c7ac-4f1d-9724-b6c3fdb76e75_1232x737.png)

## **The Attribution Play**

Attribution is key. The closer a company can get to measuring its direct impact, the more viable it becomes to shift to outcome pricing. This is the gold standard of value-based pricing: incentives fully aligned between customer and vendor, with fees justified by ROI rather than cost to serve.

From the customer perspective, outcome-based pricing also feels fairer at least in theory. Instead of paying for logins or tokens, buyers are paying in proportion to results achieved. However, in practice, attribution is hard and comes with many challenges:

- **Shared credit:** Multiple tools, processes, and people contribute to any given outcome, making it hard to isolate impact.
- **Measurement gaps:** Many organizations lack the instrumentation to track outcomes consistently and credibly.
- **Trust issues:** Customers may dispute whether outcomes are directly attributable to your product, especially in complex enterprise environments.

For example, how much credit should an AI assistant get for a closed deal when a human salesperson, CRM system, and marketing campaign all played roles? Without clarity, pricing conversations can stall or turn contentious. Companies pursuing outcome-based models must invest heavily in analytics, integrations, and transparent methodologies to make attribution defensible.

Zendesk has published detailed [documentation](https://support.zendesk.com/hc/en-us/articles/5352026794010-About-automated-resolutions-for-AI-agents) about resolution definitions. For example, for email channel “an automated resolution is counted after 72 hours of inactivity if all of the following are true:

- The AI agent provided a generative reply based on the end user’s question.
- No human agent responded to the ticket created by the end user’s request.
- The AI evaluation process confirmed that the AI agent’s response was relevant.”

Despite the benefits,buyers struggle with outcome based pricing based on A16Z [research](https://a16z.com/ai-enterprise-2025/) due to “lack of clear outcomes that map to business goals, unpredictable costs, and attribution” There are many attribution challenges today especially for workflows that are dependent on multiple products and I expect this to be a domain of opportunity and for the companies that manage to convincingly create defensible attribution models.

[](https://substackcdn.com/image/fetch/$s_!CNfC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F21ed9a5b-8ee8-49b9-bac5-0b9550c66714_1228x641.png)

## **What the Future looks like**

We’ve entered an era where traditional SaaS pricing no longer fits AI’s economics. But this isn’t uncharted territory. Each previous pricing revolution was driven by a shift in value perception.

**Guiding principles:**

- Pricing should scale with value delivered.
- Capture a portion of the value you create.
- Avoid tying pricing to costs as they are irrelevant (and change fast as new tools and platforms emerge).

Trends:

- The next wave of pricing power will go to companies that build trustworthy attribution systems, proving that their AI drives measurable results. Expect increased innovation in usage metering, cost optimization for LLMs, and attribution frameworks, similar to how FinOps evolved in the cloud era.
- Vendors with a focus on usage based pricing will double down on commitments and volume discounts to increase predictability for their revenue and their customers’ costs.

[Share](https://bmak.substack.com/p/the-era-of-ai-pricing-extended?utm_source=substack&utm_medium=email&utm_content=share&action=share)

## **References**

[Charging for Intelligence – Emergence Capital](https://www.emcap.com/thoughts/charging-for-intelligence-how-to-price-ai-software)[How to Price and Package AI SaaS Products – SaaStr](https://www.saastr.com/how-to-price-and-package-ai-saas-products/)[How AI Is Rewriting the Rules of SaaS Pricing – Metronome](https://metronome.com/blog/how-ai-is-rewriting-the-rules-of-saas-pricing)[The Economics of AI Pricing – Pilot](https://pilot.com/blog/ai-pricing-economics-2025)[A16Z: The AI Enterprise 2025 Report](https://a16z.com/ai-enterprise-2025/)