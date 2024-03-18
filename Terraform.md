








## Outputs:

* Output values are like the return values of a Terraform modules.
* Terraform outputs are used for two things: either printing details about a resource/datasource/local/variable in the command line or exporting different details about these if we are using a module.

* * Outputs are written in *"outputs.tf"* file .


    ## State:
 * The Terraform state file is a crucial component of Terraform that helps it keep track of the resources it manages and their current state. 
 * This file, often named terraform.tfstate, is a JSON or HCL (HashiCorp Configuration Language) formatted file that contains important information about the infrastructure's current state, such as resource attributes, dependencies, and metadata.


**Advantages of Terraform State File:**
____
**Resource Tracking:** The state file keeps track of all the resources managed by Terraform, including their attributes and dependencies. This ensures that Terraform can accurately update or destroy resources when necessary.

**Concurrency Control:** Terraform uses the state file to lock resources, preventing multiple users or processes from modifying the same resource simultaneously. This helps avoid conflicts and ensures data consistency.

**Plan Calculation:** Terraform uses the state file to calculate and display the difference between the desired configuration (defined in your Terraform code) and the current infrastructure state. This helps you understand what changes Terraform will make before applying them.

**Resource Metadata:** The state file stores metadata about each resource, such as unique identifiers, which is crucial for managing resources and understanding their relationships.

**Disadvantages of Storing Terraform State in Version Control Systems (VCS):**
___
**Security Risks:** Sensitive information, such as API keys or passwords, may be stored in the state file if it's committed to a VCS. This poses a security risk because VCS repositories are often shared among team members.

**Versioning Complexity:** Managing state files in VCS can lead to complex versioning issues, especially when multiple team members are working on the same infrastructure.

   **Problems with Terraform local state:**

* In case if one is using Terraform for learning like use, storing state in a single terraform.tfstate file that lives locally on your computer works jut fine. But in case you want to use Terraform in real production scenarios, one may run into several problems: -

 **Shared Storage For State Files**

* In real world scenario, multiple people will be working on the same infrastructure in. So the   team members would need access to same Terraform state files.

**Locking State Files**

* If at all you find a way to share the state files, a new problem of locking arises. In absence of   locking feature there would be problems of conflicts, loss of infra & possibility of corrupt state   files.  

**Isolating State Files**

* One will never want that any incident in the testing or staging phase to effect the real deployed infrastructure. Hence the necessity comes to isolate the changes to testing runtime, the problem arises because the entire infrastructure may be defined in a same state file.

  **Problems of storing Terraform state file in version control:**


* Most of us would be using various version controls in order to allow multiple members of your team to gain access to common resource. Although one can store Terraform files in version control but storing terraform.tfstate file in version control is not at a great idea. The reason being: -

**High Probability Of Human Error**

* In case anyone runs terraform apply with previous version of terraform.tfstate file, the entire   infrastructure will roll back to previous version, which will create an incident which was   definitely avoidable.

**Unavailability Of Locking Feature**

* Most of the available version does not provide file locking feature, as a result multiple people cannot work on the same infrastructure at same point of time.

**Leakage Of Sensitive Data**

* The terraform.tfstate file might contain sensitive data and if you would have observed a terraform.tfstate file stores data in plain text.


**Overcoming Disadvantages with Remote Backends (e.g., S3):**

A remote backend stores the Terraform state file outside of your local file system and version control. Using S3 as a remote backend is a popular choice due to its reliability and scalability. Here's how to set it up:

1. **Create an S3 Bucket**: Create an S3 bucket in your AWS account to store the Terraform state. Ensure that the appropriate IAM permissions are set up.

2. **Configure Remote Backend in Terraform:**

   ```hcl
   # In your Terraform configuration file (e.g., main.tf), define the remote backend.
   terraform {
     backend "s3" {
       bucket         = "your-terraform-state-bucket"
       key            = "path/to/your/terraform.tfstate"
       region         = "us-east-1" # Change to your desired region
       encrypt        = true
       dynamodb_table = "your-dynamodb-table"
     }
   }
   ```

   Replace `"your-terraform-state-bucket"` and `"path/to/your/terraform.tfstate"` with your S3 bucket and desired state file path.

3. **DynamoDB Table for State Locking:**

   To enable state locking, create a DynamoDB table and provide its name in the `dynamodb_table` field. This prevents concurrent access issues when multiple users or processes run Terraform.

**State Locking with DynamoDB:**

DynamoDB is used for state locking when a remote backend is configured. It ensures that only one user or process can modify the Terraform state at a time. Here's how to create a DynamoDB table and configure it for state locking:

1. **Create a DynamoDB Table:**

   You can create a DynamoDB table using the AWS Management Console or AWS CLI. Here's an AWS CLI example:

   ```sh
   aws dynamodb create-table --table-name your-dynamodb-table --attribute-definitions AttributeName=LockID,AttributeType=S --key-schema AttributeName=LockID,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
   ```

2. **Configure the DynamoDB Table in Terraform Backend Configuration:**

   In your Terraform configuration, as shown above, provide the DynamoDB table name in the `dynamodb_table` field under the backend configuration.

By following these steps, you can securely store your Terraform state in S3 with state locking using DynamoDB, mitigating the disadvantages of storing sensitive information in version control systems and ensuring safe concurrent access to your infrastructure. For a complete example in Markdown format, you can refer to the provided example below:

```markdown
# Terraform Remote Backend Configuration with S3 and DynamoDB

## Create an S3 Bucket for Terraform State

1. Log in to your AWS account.

2. Go to the AWS S3 service.

3. Click the "Create bucket" button.

4. Choose a unique name for your bucket (e.g., `your-terraform-state-bucket`).

5. Follow the prompts to configure your bucket. Ensure that the appropriate permissions are set.

## Configure Terraform Remote Backend

1. In your Terraform configuration file (e.g., `main.tf`), define the remote backend:

   ```hcl
   terraform {
     backend "s3" {
       bucket         = "your-terraform-state-bucket"
       key            = "path/to/your/terraform.tfstate"
       region         = "us-east-1" # Change to your desired region
       encrypt        = true
       dynamodb_table = "your-dynamodb-table"
     }
   }
   ```

   Replace `"your-terraform-state-bucket"` and `"path/to/your/terraform.tfstate"` with your S3 bucket and desired state file path.

2. Create a DynamoDB Table for State Locking:

   ```sh
   aws dynamodb create-table --table-name your-dynamodb-table --attribute-definitions AttributeName=LockID,AttributeType=S --key-schema AttributeName=LockID,KeyType=HASH --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
   ```

   Replace `"your-dynamodb-table"` with the desired DynamoDB table name.

3. Configure the DynamoDB table name in your Terraform backend configuration, as shown in step 1.

By following these steps, you can securely store your Terraform state in S3 with state locking using DynamoDB, mitigating the disadvantages of storing sensitive information in version control systems and ensuring safe concurrent access to your infrastructure.
```

Please note that you should adapt the configuration and commands to your specific AWS environment and requirements.