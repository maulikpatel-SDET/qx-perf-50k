"""Service module 2873: business logic, no crypto."""


def calculate_total_2873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2873():
    return 'module 2873 handles orders and invoices'
