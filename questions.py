questions = [
    "what are your business hours",
    "how can i track my order",
    "what is your return policy",
    "can i change my shipping address after placing an order",
    "what payment methods do you accept",
    "how do i reset my password",
    "do you offer international shipping",
    "what should i do if i receive a damaged item",
    "how can i contact your customer service department",
    "what is the status of my order",
    "do you offer gift wrapping services",
    "can i cancel my order",
    "how do i unsubscribe from your mailing list",
    "what are the benefits of creating an account on your website",
    "what should i do if i haven't received my order",
    "can i place an order over the phone",
    "do you offer bulk discounts for large orders",
    "how do i apply a promo code to my order",
    "what is your company's mission statement",
    "how do i check the balance on my gift card",
    "what should i do if i accidentally placed a duplicate order",
    "do you offer expedited shipping options",
    "what is your privacy policy",
    "how do i update my account information",
    "what should i do if i'm having trouble placing an order online",
    "do you offer price matching",
    "what measures do you take to ensure customer data security",
    "can i change the size/color of an item in my order before it ships",
    "how do i leave feedback about my shopping experience",
    "what is your product warranty policy",
    "do you offer installation services for your products",
    "how do i request a refund",
    "are there any restrictions on using promotional codes",
    "can i return an item without the original packaging",
    "how do i check the status of my warranty claim",
    "what should i do if i receive the wrong item in my order",
    "do you offer price adjustments if an item goes on sale after i purchase it",
    "how do i sign up for your loyalty program",
    "what should i do if i have a complaint about my shopping experience",
    "do you offer virtual assistance for troubleshooting technical issues",
    "can i place an order for pickup at a local store",
    "how do i sign up for product notifications when an item is back in stock",
    "what should i do if i'm having trouble logging into my account",
    "can i customize an item before purchasing it",
    "do you offer corporate accounts or discounts for businesses",
    "what should i do if my payment method is declined during checkout",
    "can i schedule a delivery date for my order",
    "how do i request a copy of my invoice",
    "can i get a refund if i change my mind about my purchase",
    "is there a customer service number i can call for assistance",
    "udit is known for"
]

answers = [
    "Our business hours are Monday to Friday, 9:00 AM to 5:00 PM.",
    "You can track your order by logging into your account on our website and accessing the 'Order Status' page.",
    "Our return policy allows returns within 30 days of purchase. Please refer to our website for detailed return instructions.",
    "Unfortunately, we cannot change the shipping address after an order has been placed. Please double-check your address before confirming your order.",
    "We accept payments via credit/debit cards, PayPal, and bank transfers.",
    "You can reset your password by clicking on the 'Forgot Password' link on the login page and following the instructions.",
    "Yes, we offer international shipping to select countries. Shipping fees and delivery times may vary.",
    "If you receive a damaged item, please contact our customer service department within 48 hours of delivery for assistance.",
    "You can contact our customer service department via email at support@example.com or by phone at +123-456-7890 during business hours.",
    "You can check the status of your order by logging into your account on our website and navigating to the 'Order History' section.",
    "Yes, we offer gift wrapping services for an additional fee. You can select this option during checkout.",
    "Orders can be canceled within 24 hours of placement. Please contact our customer service department for assistance.",
    "To unsubscribe from our mailing list, please click on the 'Unsubscribe' link at the bottom of any promotional email.",
    "Creating an account offers benefits such as faster checkout, order tracking, and access to exclusive offers and promotions.",
    "If you haven't received your order within the estimated delivery time, please contact our customer service department for assistance.",
    "Currently, orders can only be placed online through our website.",
    "Yes, we offer bulk discounts for large orders. Please contact our sales department for more information.",
    "You can apply a promo code to your order during checkout in the designated field.",
    "Our company's mission is to provide high-quality products and exceptional customer service to our valued customers.",
    "You can check the balance on your gift card by visiting our website and logging into your account.",
    "If you accidentally placed a duplicate order, please contact our customer service department to have one of the orders canceled.",
    "Yes, we offer expedited shipping options for an additional fee. You can select this option during checkout.",
    "Our privacy policy outlines how we collect, use, and protect customer information. Please refer to our website for details.",
    "You can update your account information by logging into your account on our website and accessing the 'Account Settings' page.",
    "If you're having trouble placing an order online, please contact our customer service department for assistance.",
    "We do offer price matching under certain conditions. Please refer to our website or contact our customer service department for more information.",
    "We employ industry-standard security measures to protect customer data, including encryption and secure server connections.",
    "You can change the size or color of an item in your order before it ships by contacting our customer service department.",
    "You can leave feedback about your shopping experience by completing our online feedback form on our website.",
    "Our product warranty policy covers manufacturing defects for a specified period. Please refer to the product documentation for details.",
    "We do not offer installation services for our products. However, we provide detailed instructions for self-installation.",
    "You can request a refund by contacting our customer service department and providing your order details.",
    "There may be restrictions on using promotional codes, such as expiration dates or product exclusions. Please check the terms and conditions associated with the code.",
    "Yes, you can return an item without the original packaging, but please ensure it's securely packaged for return shipment.",
    "You can check the status of your warranty claim by contacting our customer service department.",
    "If you receive the wrong item in your order, please contact our customer service department for assistance with a replacement or refund.",
    "We do not offer price adjustments for items that go on sale after purchase.",
    "You can sign up for our loyalty program by creating an account on our website and opting into the program.",
    "If you have a complaint about your shopping experience, please contact our customer service department to discuss your concerns.",
    "Yes, we offer virtual assistance for troubleshooting technical issues. Please contact our customer service department for assistance.",
    "Currently, we do not offer pickup options at local stores. All orders are shipped directly to the provided address.",
    "You can sign up for product notifications by subscribing to our email list or enabling notifications on our website.",
    "If you're having trouble logging into your account, please use the 'Forgot Password' link on the login page to reset your password.",
    "Customization options may vary depending on the product. Please check the product description or contact our customer service department for assistance.",
    "We offer corporate accounts and discounts for businesses. Please contact our sales department for more information.",
    "If your payment method is declined during checkout, please ensure that the information entered is correct or try an alternative payment method.",
    "You can request a delivery date for your order by contacting our customer service department after placing your order.",
    "You can request a copy of your invoice by contacting our customer service department and providing your order details.",
    "You may be eligible for a refund if you change your mind about your purchase within the specified return period. Please refer to our return policy for details.",
    "Yes, we have a customer service number for assistance. You can reach us at +123-456-7890 during business hours.",
    "black nigga randi"

]

def get_list_of_words():
    list_of_words = []
    for question in questions:
        list_of_words.append(question.split(" "))
    return list_of_words
