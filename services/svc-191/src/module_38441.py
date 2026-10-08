"""Service module 38441: business logic, no crypto."""


def calculate_total_38441(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38441():
    return 'module 38441 handles orders and invoices'
