## What is Internet gateway in AWS?

An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet. It supports IPv4 and IPv6 traffic. It does not cause availability risks or bandwidth constraints on your network traffic.

An internet gateway enables resources in your public subnets (such as EC2 instances) to connect to the internet if the resource has a public IPv4 address or an IPv6 address. Similarly, resources on the internet can initiate a connection to resources in your subnet using the public IPv4 address or IPv6 address. For example, an internet gateway enables you to connect to an EC2 instance in AWS using your local computer.

An internet gateway provides a target in your VPC route tables for internet-routable traffic. For communication using IPv4, the internet gateway also performs network address translation (NAT). For communication using IPv6, NAT is not needed because IPv6 addresses are public.
***

**What are route tables in AWS?**
---
A route table contains a set of rules, called routes, that determine where network traffic from your subnet or gateway is directed.
* Route tables are the one that defines how to route the traffic within the subnet.

**Route table concepts**

The following are the key concepts for route tables.

•	Main route table—The route table that automatically comes with your VPC. It controls the routing for all subnets that are not explicitly associated with any other route table.

•	Custom route table—A route table that you create for your VPC.

•	Destination—The range of IP addresses where you want traffic to go (destination CIDR). For example, an external corporate network with the CIDR 172.16.0.0/12.

•	Target—The gateway, network interface, or connection through which to send the destination traffic; for example, an internet gateway.

•	Route table association—The association between a route table and a subnet, internet gateway, or virtual private gateway.

•	Subnet route table—A route table that's associated with a subnet.

•	Local route—A default route for communication within the VPC.

•	Propagation—If you've attached a virtual private gateway to your VPC and enable route propagation, we automatically add routes for your VPN connection to your subnet route tables. This means that you don't need to manually add or remove VPN routes. For more information, see Site-to-Site VPN routing options in the Site-to-Site VPN User Guide.

•	Gateway route table—A route table that's associated with an internet gateway or virtual private gateway.

•	Edge association—A route table that you use to route inbound VPC traffic to an appliance. You associate a route table with the internet gateway or virtual private gateway, and specify the network interface of your appliance as the target for VPC traffic.

•	Transit gateway route table—A route table that's associated with a transit gateway. For more information, see Transit gateway route tables in Amazon VPC Transit Gateways.

•	Local gateway route table—A route table that's associated with an Outposts local gateway. For more information, see Local gateways in the AWS Outposts User Guide.

VPC
---
Imagine you want to set up a private, secure, and isolated area in the cloud where you can run your applications and store your data. This is where a VPC comes into play.

A VPC is a virtual network that you create in the cloud. It allows you to have your own private section of the internet, just like having your own network within a larger network. Within this VPC, you can create and manage various resources, such as servers, databases, and storage.

**Features:**

The following features help you configure a VPC to provide the connectivity that your applications need:
Virtual private clouds (VPC)
A VPC is a virtual network that closely resembles a traditional network that you'd operate in your own data center. After you create a VPC, you can add subnets.

  **COMPONENTS:**

**Subnets:**

A subnet is a range of IP addresses in your VPC. A subnet must reside in a single Availability Zone. After you add subnets, you can deploy AWS resources in your VPC.

**IP addressing:**

You can assign IP addresses, both IPv4 and IPv6, to your VPCs and subnets. You can also bring your public IPv4 addresses and IPv6 GUA addresses to AWS and allocate them to resources in your VPC, such as EC2 instances, NAT gateways, and Network Load Balancers.

**Routing:**

Use route tables to determine where network traffic from your subnet or gateway is directed.

**Gateways and endpoints:**

A gateway connects your VPC to another network. For example, use an internet gateway to connect your VPC to the internet. Use a VPC endpoint to connect to AWS services privately, without the use of an internet gateway or NAT device.

**Peering connections:**

Use a VPC peering connection to route traffic between the resources in two VPCs.

**Traffic Mirroring:**

Copy network traffic from network interfaces and send it to security and monitoring appliances for deep packet inspection.

**Transit gateways:**

Use a transit gateway, which acts as a central hub, to route traffic between your VPCs, VPN connections, and AWS Direct Connect connections.

**VPC Flow Logs:**

A flow log captures information about the IP traffic going to and from network interfaces in your VPC.

**VPN connections:**

Connect your VPCs to your on-premises networks using AWS Virtual Private Network (AWS VPN).
***
SECURITY GROUPS 
---
Security groups are applied at the instance level.
Security groups are meant to open only specific ports and allow only the specific traffic into the ec2 instance.

ROUTE 53 
---
Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. Route 53 connects user requests to internet applications running on AWS or on-premises.

*DNS maps the domain name with the IP address or DNS is the one that resolves the domain name with the IP address.
### But in real world scenarion DNS resolves Domain name to the loadbalencer IP address only.

You can use Route 53 to perform three main functions in any combination: domain registration, DNS routing, and health checking.
If you choose to use Route 53 for all three functions, be sure to follow the order below:

1. Register domain names
Your website needs a name, such as example.com. Route 53 lets you register a name for your website or web application, known as a domain name.
•	For an overview, see How domain registration works.
•	For a procedure, see Registering a new domain.
•	For a tutorial that takes you through registering a domain and creating a simple website in an Amazon S3 bucket, see Getting started with Amazon Route 53.


2. Route internet traffic to the resources for your domain
When a user opens a web browser and enters your domain name (example.com) or subdomain name (acme.example.com) in the address bar, Route 53 helps connect the browser with your website or web application.
•	For an overview, see How internet traffic is routed to your website or web application.
•	For procedures, see Configuring Amazon Route 53 as your DNS service.
•	For a procedure on how to route email to Amazon WorkMail, see Routing traffic to Amazon WorkMail.


3. Check the health of your resources
Route 53 sends automated requests over the internet to a resource, such as a web server, to verify that it's reachable, available, and functional. You also can choose to receive notifications when a resource becomes unavailable and choose to route internet traffic away from unhealthy resources.
•	For an overview, see How Amazon Route 53 checks the health of your resources.
•	For procedures, see Creating Amazon Route 53 health checks and configuring DNS failover.

-----------------------------------------------------------------------------------------------------------------

