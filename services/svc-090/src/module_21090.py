"""Service module 21090: business logic, no crypto."""


def calculate_total_21090(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21090():
    return 'module 21090 handles orders and invoices'
