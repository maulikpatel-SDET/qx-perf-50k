"""Service module 28873: business logic, no crypto."""


def calculate_total_28873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28873():
    return 'module 28873 handles orders and invoices'
