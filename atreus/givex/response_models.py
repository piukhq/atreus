from pydantic import BaseModel


class PointsTransaction(BaseModel):
    transaction_local_date: str
    transaction_local_time: str
    transaction_type: str
    points: str
    store_name: str
    points_amount: str
    pointsskudetail_element: list[str]
    transaction_id: str
    channel_id: str
    transaction_server_datetime: str
    visit_datetime: str
    transaction_type_id: str
    operator: str
    store_user: str
    promo_code: str
    base_points: str
    tier_bonus_points: str
    promo_code_points: str
    tier_id: str


class Givex911Response(BaseModel):
    transaction_code: str
    result: str
    givex_transaction_reference: str
    error_message: str
    points_added: str
    points_balance: str
    certificate_balance: str
    member_name: str
    receipt_message: str
    discount_amount: str
    iso_serial: str
    unit_balance: str
    loyalty_balance: str
    certificate_expiration_date: str
    transaction_code: str
    result: str
    givex_transaction_reference: str
    error_message: str
    points_added: str
    points_balance: str
    certificate_balance: str
    member_name: str
    receipt_message: str
    discount_amount: str
    iso_serial: str
    unit_balance: str
    loyalty_balance: str
    certificate_expiration_date: str


class Givex945Response(BaseModel):
    transaction_code: str
    result: str
    error_message: str
    givex_transaction_reference: str
    points_removed: str
    points_balance: str
    iso_serial: str


class Givex946Response(BaseModel):
    transaction_code: str
    result: str
    error_message: str
    customer_id: str
    customer_first_name: str
    customer_last_name: str
    customer_reg_date: str
    iso_serial: str
    loyalty_enroll_id: str
    login_token: str
    customer_reference: str
    otp_key: str
    otp_url: str
    email_verification_status: str


class Givex995Response(BaseModel):
    transaction_code: str
    result: str
    error_message: str
    certificate_balance: str
    currency: str
    points_balance: str
    transhist: list = []
    totalrows: str
    iso_serial: str
    certificate_expiration_date: str
    operator_message: str


class Givex996Response(BaseModel):
    transaction_code: str
    result: str
    error_message: str
    member_address: str
    member_mobile: str
    member_email: str
    member_birthdate: str
    sms_contact_number: str
    email_contact_answer: str
    mail_contact_answer: str
    member_phone: str
    referring_member_name: str
    member_title: str
    iso_serial: str
    purchase_amount_to_next_tier: str
    purchase_amount_email_curreny_tier: str
    purchase_amount_via_default_promo_code: str
    date_of_the_last_tier_change: str
    amount_spent_since_last_tier_change: str
    message_type: str
    message_delivery_method: str
    points_to_earn_to_reach_next_tier: str
    points_to_earn_to_remain_in_current_tier: str
    total_points_earned_since_last_upgrade: str
    next_points_to_money_automatic_conversion_threshold: str
    points_required_for_next_points_to_money_automatic_conversion: str
    tier_id: str
    tier_name: str
