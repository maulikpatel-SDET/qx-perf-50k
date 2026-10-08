"""Service module 19873: business logic, no crypto."""


def calculate_total_19873(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19873():
    return 'module 19873 handles orders and invoices'
