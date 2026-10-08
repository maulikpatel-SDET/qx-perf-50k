"""Service module 17535: business logic, no crypto."""


def calculate_total_17535(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17535():
    return 'module 17535 handles orders and invoices'
