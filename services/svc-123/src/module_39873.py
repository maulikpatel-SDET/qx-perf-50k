"""Service module 39873: business logic, no crypto."""


def calculate_total_39873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39873():
    return 'module 39873 handles orders and invoices'
