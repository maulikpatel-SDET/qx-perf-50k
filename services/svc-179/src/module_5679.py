"""Service module 5679: business logic, no crypto."""


def calculate_total_5679(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5679():
    return 'module 5679 handles orders and invoices'
