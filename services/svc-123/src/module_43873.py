"""Service module 43873: business logic, no crypto."""


def calculate_total_43873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43873():
    return 'module 43873 handles orders and invoices'
