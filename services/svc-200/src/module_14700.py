"""Service module 14700: business logic, no crypto."""


def calculate_total_14700(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14700():
    return 'module 14700 handles orders and invoices'
