### :bread: AWS Resources 
1. Create a DynamoDB table
https://console.aws.amazon.com/dynamodb/home?region=us-east-1#create-table:

    Table name: magiclink
    
    Primary key: id (String)

2. Create 6 lambda functions

    a. defineAuthChallenge - runtime: nodeJs 14.x, use following code
    https://github.com/solariswu/aws-cognito-custom-auth-flow/blob/main/magicLink/cdk/lambda/definechallenge/defineauthchallenge.js

    lambda execution role for this lambda : AWSLambdaBasicExecutionRole

    b. createAuthChallenge - runtime: nodeJs 14.x, use following code
    https://github.com/solariswu/aws-cognito-custom-auth-flow/blob/main/magicLink/cdk/lambda/createchallenge/createauthchallenge.js

    lambda execution role for this lambda : AWSLambdaBasicExecutionRole

    c. verifyAuthChallenge - runtime: python 3.7, use following code
    https://github.com/solariswu/aws-cognito-custom-auth-flow/blob/main/magicLink/cdk/lambda/verifychallenge/verifyauthchallenge.py

    lambda execution role for this lambda : AWSLambdaBasicExecutionRole + dynamodb:GetItem

    Add the layer of requests lib for your python
    https://aws.amazon.com/blogs/compute/upcoming-changes-to-the-python-sdk-in-aws-lambda/


    d. preSignUp - runtime: nodeJs 14.x
    https://github.com/solariswu/aws-cognito-custom-auth-flow/blob/main/magicLink/cdk/lambda/presignup/presignuplambda.js

    lambda execution role for this lambda : AWSLambdaBasicExecutionRole

    e. magiclink - runtime: python3.7
    https://github.com/solariswu/aws-cognito-custom-auth-flow/blob/main/magicLink/cdk/lambda/magiclink/magiclink.py

    Note: :zap: need to replace the sender email address and the application url with your own's.
    Both the sender email and the receiptor's email address require verified in SES. 

    I use adminRole for this execution. You may fine tune the permission. 

    f. magicresponse - runtime: python3.7
    https://github.com/solariswu/aws-cognito-custom-auth-flow/blob/main/magicLink/cdk/lambda/magicresponse/magicresponse.py

    Note: :zap: need to replace the userpool id, client id with your own's
    
    I use adminRole for this execution. You may fine tune the permission. 


3. create APIGateway resource
    a. https://yourapigateway_domain.com/magiclink
    use the magiclink lambda as the backend. 
    b. https://yourapigateway_domain.com/magicresponse
    use the magicresponse lambda as the backend. 

4. SES account, if your account is still in sandbox, the test's email address and the send email address in the magiclink lambda are required to be verified in the SES services. 

5. Add lambdas to your userpool's DefineAuthChallenge, CreateAuthChallenge and VerifyAuthChallange lambda triggers in the User Pool AWS Console. 

6. change the aws resource config to include your user pool's. 
    https://github.com/solariswu/aws-cognito-custom-auth-flow/blob/main/magicLink/vue/src/aws-exports.js

7. change the App code
    https://github.com/solariswu/aws-cognito-custom-auth-flow/blob/main/magicLink/vue/src/views/Hogwarts.vue#L36

    https://github.com/solariswu/aws-cognito-custom-auth-flow/blob/main/magicLink/vue/src/views/Hogwarts.vue#L42

    https://github.com/solariswu/aws-cognito-custom-auth-flow/blob/main/magicLink/vue/src/views/Login.vue#L52

=== Link IdP users with Userpool users ===

8. Create a lambda function restlinkuser - Runtime Nodejs 14
    
    https://github.com/solariswu/aws-cognito-custom-auth-flow/blob/main/magicLink/cdk/lambda/magiclinkuser/restlinkuser.js    

    lambda execution role for this lambda : AWSLambdaBasicExecutionRole + cognito-idp:adminLinkUser + cognito-idp:listuser + cognito-idp:deleteuser

9. Create a new path under APIGateway 
    
    API path - https://yourapigateway_domain.com/linkuser
    
    create Method "GET"
    
    use the restlinkuser lambda as the backend, ensure tick the ***"Use Lambda Proxy integration"*** - YES
    
    set up Userpool authorizor for this GET method. 

10. Create a new path under APIGateway
    
    API path. https://yourapigateway_domain.com/valiatetoken
    
    Method Get
    
    choose 'Mock' as the integration type of this method.
    
    set up Userpool authorizor for this GET method.
 
 
=== Change forgot password / reset password to email link instead of email code ===

11. Create a new lambda function. It would require to be set in the userpool's Custom message lambda trigger.

    https://github.com/solariswu/aws-cognito-custom-auth-flow/blob/main/magicLink/cdk/lambda/customForgotPwd.js
    
    Runtime - NodeJs 14 - execution role - AWSLambdaBasicExecutionRole

### Project setup
```
npm install
```
### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```
