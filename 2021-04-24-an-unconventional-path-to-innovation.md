# An unconventional path to innovation


**Published:** 2021-04-24  
**Source:** [https://bmak.substack.com/p/an-unconventional-path-to-innovation](https://bmak.substack.com/p/an-unconventional-path-to-innovation)

---

**From monoliths to microservices**

Back in the day, most applications were built based on a monolithic architecture. Monolithic - in Greek meaning “one rock” - refers to an application which is developed as a single unit. This can be a fast way to develop the first version of a product as the team is relatively small and can easily coordinate.

The challenges come with scale. Product development starts requiring more coordination, as several teams work on the same code base. Architecture becomes complicated and newer team members, who are naturally not familiar with all parts of the application, create additional risk with every new deployment. Seemingly straightforward code changes can have huge unintended consequences to other parts of the application, so change is slow as it requires thorough testing across systems.

The pain was real so engineers went on to find better ways to develop applications. The first ideas around Service Oriented Architecture (SOA) started to emerge around the early 90s, and evolved to what we today know as microservices. The main innovation was to design applications in a modular way. Each application can consist of several components (services) that serve discrete business functions and are “loosely coupled”, meaning they require little or no knowledge of the definitions of other separate components.

*Image by [Four Blair Services](https://commons.wikimedia.org/wiki/File:Services4.png)*

In the most recent years, microservices have become mainstream, with 63% of companies reporting that they are using microservices according to a [survey](https://www.globenewswire.com/news-release/2018/09/20/1573625/0/en/New-Research-Shows-63-Percent-of-Enterprises-Are-Adopting-Microservices-Architectures-Yet-50-Percent-Are-Unaware-of-the-Impact-on-Revenue-Generating-Business-Processes.html) of 354 enterprises. These new design patterns offer several benefits that address the scaling challenges of a monolithic design. With the introduction of a modular design principle, microservices follow a logic of developing separate components for each business function, simplifying and speeding up development by:

- Minimizing dependencies between services
- Simplifying the overall service architecture
- Enabling parallelization of work
- Reducing the scope of testing

This evolution might one day be taught in some Software Engineering History course, but why should we care? The most common answer is that this new approach provides massive efficiency benefits in the software development process. While this is true, there is an even more important reason. **Microservices enable a company wide modularity that goes beyond a tech mandate. It is a shift to how teams are expected to interact and innovate at scale.**

[Share](https://bmak.substack.com/p/an-unconventional-path-to-innovation?utm_source=substack&utm_medium=email&utm_content=share&action=share)

**The Amazon story**

Amazon was founded in 1994 and was publicly listed three years later. Between 1997 and 2000 Amazon revenue grew from $148MM to $2.76Bn, a 18.6x increase. At the same time headcount increased from 614 to 9,000 employees, a 14.6x increase.

 This revenue increase was great news for the newly founded e-commerce startup, but came at a cost. The growth also started increasing complexity which in turn slowed things down. The mechanics of this process are quite simple: any new initiative increases the overall complexity of the system; in the now larger system, any new initiative requires code changes and coordination across several teams for understanding different architectures and deploying changes. As a result, growth is a vicious circle that increases the coordination tax and slows down future development and innovation.

Seemingly straightforward features have to be carefully planned and deployed, requiring other teams’ support, as a small mistake can bring down the whole business. Former Amazon VP Colin Bryar, gives a good example of how a simple change in the Amazon Associates program referral fee logic could introduce bugs that could bring down Amazon.com as all teams shared the same code and database.

A traditional response to this problem is to start introducing processes and control mechanisms, while hiring more gatekeepers and coordinators. Among other initiatives, Amazon introduced a small group of “database gatekeepers” who were reviewing any change request that impacted the massive Amazon database. While this minimized the probability of a large scale event, it slowed down teams even further.

A more groundbreaking approach is to eliminate the need for coordination. In their excellent book “[Working Backwards](https://www.amazon.com/Working-Backwards-Insights-Stories-Secrets/dp/1250267595)”, Colin Bryar and Bill Carr give more context. “In my tenure at Amazon I heard Jeff say many times that if we wanted Amazon to be a place where builders can build, we needed to eliminate communication, not encourage it. When you view effective communication across groups as a “defect,” the solutions to your problems start to look quite different from traditional ones”. Bezos’s idea was to substitute the need for human to human coordination with machine to machine communication through APIs. While this sounds counterintuitive, more coordination is only slowing down things even further.

So Jeff gave a mandate for all teams to support this new initiative. Steve Yegge, who during the early 2000s was a Software Development Manager at Amazon, [gives some detail](https://gist.github.com/chitchcock/1281611):

*“On one occasion -- back around 2002 I think, plus or minus a year -- he (Jeff Bezos) issued a mandate that was so out there, so huge and eye-bulging ponderous, that it made all of his other mandates look like unsolicited peer bonuses. His Big Mandate went something along these lines:*

- *All teams will henceforth expose their data and functionality through service interfaces.*
- Teams must communicate with each other through these interfaces.
- There will be no other form of interprocess communication allowed: no direct linking, no direct reads of another team's data store, no shared-memory model, no back-doors whatsoever. The only communication allowed is via service interface calls over the network.
- It doesn't matter what technology they use. HTTP, Corba, Pubsub, custom protocols -- doesn't matter. Bezos doesn't care.
- All service interfaces, without exception, must be designed from the ground up to be externalizable. That is to say, the team must plan and design to be able to expose the interface to developers in the outside world. No exceptions.
- Anyone who doesn't do this will be fired.
- Thank you; have a nice day!”

Migrating to a microservice architecture doesn’t happen overnight. Werner Vogels who later became Amazon’s CTO gives more color in this 2006 [interview](https://queue.acm.org/detail.cfm?id=1142065):

> *“The big architectural change that Amazon went through in the past five years was to move from a two-tier monolith to a fully-distributed, decentralized, services platform serving many different applications. (...) It has been a major learning experience, but we have now reached a point where it has become one of our main strategic advantages. We can now build very complex applications out of primitive services that are by themselves relatively simple. We can scale our operation independently, maintain unparalleled system availability, and introduce new services quickly without the need for massive reconfiguration.”*

However, transitioning to a microservices architecture is a necessary but not sufficient condition to solving this problem. An organization also needs the right team structure to ensure the initiative’s success. After a lot of iterations Amazon teams evolved to what was initially known as the “two pizza team” model - small enough teams that could be fed with two large pizzas. Not surprisingly, the main characteristics of these teams are very similar to the microservices principles: small, autonomous, and owning both business and tech in their space.

**Velocity matters in business**

*Image by [Lukas Raich](https://commons.wikimedia.org/wiki/File:FIA_F1_Austria_2018_Nr._33_Verstappen.jpg#filelinks)*

> *“Speed, or more accurately velocity, which measures both speed and direction, matters in business. With all other things being equal, the organization that moves faster will innovate more, simply because it will be able to conduct a higher number of experiments per unit of time"*
>
> - Colin Bryar and Bill Carr (Working backwards)

 What this accomplishes is a combination of speed increase, ownership improvement, and risk reduction. All key requirements for innovation.

- **Speed:** At its core, this new pattern decouples the development process, which has a significant impact on speed of development. Any monolith development is very slow as for every new feature where two or more teams overlap, they need to serialize work and pay a huge coordination cost. If the same feature is composed of microservices, teams are able to parallelize the work with each team working on the specific services they own. This not only speeds up the actual development time, but also saves time required for team coordination, understanding of their systems, and designing a compatible service. By design microservices contain all business logic and complexity, without exposing any implementation details to its consumers. As a result, development for future consumers of this microservice is faster. Lastly, a modular design results in more clean and understandable architectures, which speed up future iterations and testing.
- **Ownership:** The idea that a team owns their microservices, enforces better design decisions in the long term as the team knows that they will have to deal with operational issues and maintenance. Amazon applies a “You build it, you run it” logic, where teams are fully responsible for the services they own. As [Martin Fowler](https://martinfowler.com/articles/microservices.html) puts it: *“Being woken up at 3am every night by your pager is certainly a powerful incentive to focus on quality when writing your code.”* In addition to the first order effects of direct ownership, teams are also more flexible to take domain specific decisions that better fit their needs, which would not be possible with a more centralized decision making system.
- **Risk management:** The third pillar of this architecture is the concept of failure isolation. If a microservice is down for some reason, this will only affect the specific service while the rest of the application will continue to operate. While bugs are not ideal, this is a much better pattern of handling them than bringing the whole system down. Imagine an experience where a social networking site includes a functionality for adding new friends. If this is designed as a microservice and for some reason it is down, this will not impact the broader social network’s availability for users and the majority of them will not even notice the issue if they don’t use the “add friends” feature that day.

The combination of microservices and the two pizza team model was a huge success as it enabled Amazon to innovate at scale. Being loosely coupled spurs innovation as it allows teams to develop quick prototypes and reduce the go to market time by eliminating dependencies and several layers of approval. **The end result is a better product because teams can iterate faster, learn faster, and incorporate these learnings in the product at a faster pace during the same amount of time.** The core decisions for a new service are owned by the team that develops it, which increases the sense of ownership and bottom up innovation. Finally, the risk of every new product is minimized as the limited blast radius makes it less likely that a bug will impact the overall health of the system.

**Externalizing APIs as a business model**

Amazon definitely took advantage of the additional efficiency but they didn’t stop there. A direct consequence of this distributed model was the ability to extend product lines or launch new products with limited internal coordination. Several Amazon initiatives benefited by reusing already established services and APIs to scale fast. You probably are aware of the expansion of Amazon Retail from US books to a global everything store.

Another case study is the launch of Prime Now, the Amazon ultrafast delivery service in [just 111 days](https://www.inc.com/greg-satell/the-secret-behind-amazons-uncanny-ability-to-out-innovate-just-about-every-other-company-on-planet.html). The new service required the development of some new components, but several pieces of the functionality like search, add to cart, checkout flow and payments processing, were already developed by Amazon.com. The team plugged in to the existing APIs where possible, while developing the incremental services needed for supporting the new use case.

Benedict Evans in [Another Podcast](https://makrynikolas.com/Episode%20Bezos%20and%20the%20Amazon%20machine) makes a great point on this topic.

> *“Amazon is a massively decentralized swarm where everything is an API. (...) When a team wants to launch something new (e.g. German shoes team), they just plug into existing APIs and don’t need a meeting to put the request to a logistics team’s roadmap. The reason this is important is that you can add products almost indefinitely without having to multiply levels of a middle management layer and coordination cost. Amazon is a machine to make more Amazon.”*

Even stopping here one would deem this a success, but when Amazon thinks big, they mean really big. Part of this story is how Amazon invented the business model of externalizing APIs and did that time and time again with great success.

One such example is AWS. The idea that compute, memory, storage, and other primitives could be sold as a utility is groundbreaking. Amazon started offering these primitives to internal teams and eventually decided to externalize to other companies. The externalization of these APIs (already tested by several Amazon teams) was the beginning of the modern cloud. Today AWS services power millions of customers including Amazon.com. AWS 2020 [revenue was $45Bn](https://www.statista.com/statistics/250520/forecast-of-amazon-web-services-revenue/).

Another example is the Amazon marketplace. Amazon experimented by opening their platform to third party sellers, allowing them to sell side by side with their Retail business. This was accomplished by externalizing APIs for - among other things - adding selection, setting prices, and managing inventory. While controversial at the time, this proved to be a great decision. Amazon [marketplace revenue for 2020 was $80Bn](https://www.statista.com/statistics/259782/third-party-seller-share-of-amazon-platform/#:~:text=In%202020%2C%20Amazon%20generated%2080.46,dollars%20in%20the%20previous%20year.).

Byrne Hobart of the [Diff](https://diff.substack.com/p/four-refoundings) (one of the best substacks out there) sums it up nicely:

> *“Building Amazon as a bookstore was a smart decision, but backing out the abstraction - Amazon as a collection of business Lego blocks that can be broken down and rebuilt for other purposes - was one of the best strategic choices of all time. It's unclear if something like this was always the plan, or if it's an example of a technical person insisting on creating the general solution, but in terms of market value added and consumer surplus generated, it's an extraordinary refounding.”*

**Note:**For Greek speakers, I gave a talk based on this post in [JHUG Meetup](https://www.jhug.gr/jhug-meetup-april-22th-2021/) which you can watch [here](https://vimeo.com/540659777).

[Subscribe now](https://bmak.substack.com/subscribe?)