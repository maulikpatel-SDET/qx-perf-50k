"""Service module 16873: business logic, no crypto."""


def calculate_total_16873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16873():
    return 'module 16873 handles orders and invoices'
