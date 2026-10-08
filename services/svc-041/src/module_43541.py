"""Service module 43541: business logic, no crypto."""


def calculate_total_43541(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43541():
    return 'module 43541 handles orders and invoices'
