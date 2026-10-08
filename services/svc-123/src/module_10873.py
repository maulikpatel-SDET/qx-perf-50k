"""Service module 10873: business logic, no crypto."""


def calculate_total_10873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10873():
    return 'module 10873 handles orders and invoices'
