"""Service module 38105: business logic, no crypto."""


def calculate_total_38105(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38105():
    return 'module 38105 handles orders and invoices'
