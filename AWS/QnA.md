### 1)What is VPC?
A Virtual Private Cloud (VPC) is a logically isolated network within the AWS
cloud that you define. You can launch AWS resources, such as Amazon EC2 instances, into
the VPC. It provides complete control over the network configuration, including selection of
IP address range, creation of subnets, and configuration of route tables and gateways

**Flowchart:**
1. Define the IP address range
2. Create subnets
3. Configure route tables
4. Attach gateways

### 2) How to define a public and private subnet in vpc
To define public and private subnets in a VPC, you need to create subnets and
configure their route tables accordingly. A public subnet has a route to an Internet Gateway,
while a private subnet does not.
* Public Subnet: A subnet with a route to the internet through an Internet Gateway. This enables instances in this subnet to be directly accessible from the internet.

* Private Subnet: A subnet without a direct route to the internet. Instances in this subnet can access the internet via a NAT Gateway, ensuring they are not directly exposed to the internet

### 3)How an EC2 instance can fetch something from the internet
An EC2 instance can fetch data from the internet by being placed in a public
subnet with a route to an Internet Gateway. The instance also needs to have a public IP
address or be associated with an Elastic IP. Additionally, the security group must allow
outbound internet traffic.

### 4)How does a request from the app go to the internet?
A request from an app on an EC2 instance goes to the internet through a public
subnet with a route to an Internet Gateway. The instance needs a public IP address or be
associated with an Elastic IP. The security group must allow outbound traffic, and the
Network Access Control List (NACL) should also permit the traffic.

**Steps for an App Request to Reach the Internet**

1.Instance in the Subnet:

* The application running on an instance (EC2) in either a public or private subnet initiates an outbound request to the internet.

2.Route Table Lookup:

* The instance's network interface sends the request to the subnet's route table to determine the next hop for the traffic.

**For Instances in a Public Subnet:**

3.Route Through Internet Gateway:

* The route table for the public subnet includes a route directing 0.0.0.0/0 (all internet traffic) to an Internet Gateway (IGW).
The request is forwarded to the Internet Gateway.

4.Internet Gateway:

* The IGW serves as a bridge between the VPC and the internet, allowing bi-directional communication.
* The request is then routed to the internet.

5.Destination:

* The request reaches the target server on the internet, and the server processes the request and sends a response back.

6.Return Path:

* The response follows the reverse path, reaching the IGW, which forwards it to the appropriate instance in the public subnet.

**For Instances in a Private Subnet:**

3.Route Through NAT Gateway/Instance:

* The route table for the private subnet directs 0.0.0.0/0 traffic to a NAT Gateway (or NAT Instance) placed in a public subnet.
* The request is forwarded to the NAT Gateway.

4.NAT Gateway:

* The NAT Gateway allows outbound traffic to the internet while blocking inbound traffic initiated from the internet, providing an additional layer of security.
* The NAT Gateway forwards the request to the Internet Gateway.

5,Internet Gateway:

* Similar to the public subnet, the IGW forwards the request to the internet.

6.Destination:

* The request reaches the target server on the internet, and the server processes the request and sends a response back.

7.Return Path:

* The response follows the reverse path, reaching the IGW, then the NAT Gateway, which forwards it to the appropriate instance in the private subnet.

### 5. If you restrict the security group, NACL and the NAT Gateways then, how can you connect and fetch something from S3?

To connect and fetch data from Amazon S3 while having restricted Security Groups, Network Access Control Lists (NACLs), and NAT Gateways, you can leverage a VPC endpoint for S3. A VPC endpoint for S3 allows you to establish a private connection between your VPC and S3 without needing an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.

Flowchart:
1. Create VPC Endpoint for S3
2. Configure Route Table to use VPC Endpoint
3. Update Security Group and NACL




