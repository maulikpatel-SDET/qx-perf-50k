"""Service module 10899: business logic, no crypto."""


def calculate_total_10899(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10899():
    return 'module 10899 handles orders and invoices'
