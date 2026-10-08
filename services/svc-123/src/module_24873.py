"""Service module 24873: business logic, no crypto."""


def calculate_total_24873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24873():
    return 'module 24873 handles orders and invoices'
