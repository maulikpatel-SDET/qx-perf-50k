"""Service module 9873: business logic, no crypto."""


def calculate_total_9873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9873():
    return 'module 9873 handles orders and invoices'
