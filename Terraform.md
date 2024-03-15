








## Outputs:

* Output values are like the return values of a Terraform modules.
* Terraform outputs are used for two things: either printing details about a resource/datasource/local/variable in the command line or exporting different details about these if we are using a module.

* * Outputs are written in *"outputs.tf"* file .


    ## State:

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
