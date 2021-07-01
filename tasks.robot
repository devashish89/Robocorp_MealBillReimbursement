*** Settings ***
Documentation   Document Understanding + Database + Email Notification
Library    RPA.Database
Library    String
Library    RPA.FileSystem
Library    query_database.py
Library    read_env_file.py
Library    invoice_extraction.py
Library    insert_record.py
Library    RPA.Tables
Library    RPA.Email.ImapSmtp    smtp_server=smtp.gmail.com    smtp_port=587


# +
*** Keywords ***
Send email comm
    [Arguments]  ${Body}
    ${USERNAME}=    read_env_file.Get Secret Value    gmail_username
    ${PASSWORD}=    read_env_file.Get Secret Value    gmail_password
    ${RECIPIENT}=    read_env_file.Get Secret Value    to_mail
    Authorize    account=${USERNAME}    password=${PASSWORD}
    Send Message    sender=${USERNAME}
    ...    recipients=${RECIPIENT}
    ...    subject=Reimbursement has been submitted into system
    ...    body=${Body}
    

    
# -

*** Tasks ***
Raise Amt Reimbursement Task
    
    @{lst}=    List Directories In Directory  ${CURDIR}${/}Invoices
    
    FOR    ${item}    IN    @{lst}
        ${val}=    Convert To String  ${item}
        ${f}=    Split String  ${val}  ${/}
        ${username_emp}=    Convert To String  ${f}[-1]
        LOG  ${username_emp}
        
        ${email}=    Catenate   SEPARATOR=${EMPTY}  ${username_emp}  @abc.com
        LOG  ${email}
        
        #get emp name

        ${empname}=    Get Empname  ${email}
        
        
        @{lst_files}=   List Files In Directory  ${item}
        
        FOR    ${file}    IN    @{lst_files}
            Log    ${file}
            
            @{invoice_details}=    Get Invoice Details  ${file}
            
            Insert Data    ${empname}    ${email}    ${invoice_details[0]}    ${invoice_details[1]}    ${invoice_details[4]}    ${invoice_details[3]}    ${invoice_details[2]}
            
            Send email comm    Hi ${empname}, ${\n}Your reimbursement has been submitted for amount-${invoice_details[0]} successfully.${\n}Thanks,${\n}BOT
        END
       
    END
