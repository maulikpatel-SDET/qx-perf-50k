"""Service module 13873: business logic, no crypto."""


def calculate_total_13873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13873():
    return 'module 13873 handles orders and invoices'
