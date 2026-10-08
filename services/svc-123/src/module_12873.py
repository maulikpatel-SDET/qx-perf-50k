"""Service module 12873: business logic, no crypto."""


def calculate_total_12873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12873():
    return 'module 12873 handles orders and invoices'
