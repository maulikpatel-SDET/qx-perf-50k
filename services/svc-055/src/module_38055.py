"""Service module 38055: business logic, no crypto."""


def calculate_total_38055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38055():
    return 'module 38055 handles orders and invoices'
