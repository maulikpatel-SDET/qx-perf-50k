"""Service module 43100: business logic, no crypto."""


def calculate_total_43100(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43100():
    return 'module 43100 handles orders and invoices'
