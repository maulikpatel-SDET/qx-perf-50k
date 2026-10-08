"""Service module 47873: business logic, no crypto."""


def calculate_total_47873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47873():
    return 'module 47873 handles orders and invoices'
