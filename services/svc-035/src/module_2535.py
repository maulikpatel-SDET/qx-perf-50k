"""Service module 2535: business logic, no crypto."""


def calculate_total_2535(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2535():
    return 'module 2535 handles orders and invoices'
