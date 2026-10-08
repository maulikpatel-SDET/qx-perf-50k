"""Service module 31352: business logic, no crypto."""


def calculate_total_31352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31352():
    return 'module 31352 handles orders and invoices'
