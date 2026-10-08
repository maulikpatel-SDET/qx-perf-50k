"""Service module 43436: business logic, no crypto."""


def calculate_total_43436(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43436():
    return 'module 43436 handles orders and invoices'
