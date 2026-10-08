"""Service module 26873: business logic, no crypto."""


def calculate_total_26873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26873():
    return 'module 26873 handles orders and invoices'
