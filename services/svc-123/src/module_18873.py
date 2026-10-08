"""Service module 18873: business logic, no crypto."""


def calculate_total_18873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18873():
    return 'module 18873 handles orders and invoices'
