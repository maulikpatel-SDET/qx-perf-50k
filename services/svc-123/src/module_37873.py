"""Service module 37873: business logic, no crypto."""


def calculate_total_37873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37873():
    return 'module 37873 handles orders and invoices'
