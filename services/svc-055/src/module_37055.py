"""Service module 37055: business logic, no crypto."""


def calculate_total_37055(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37055():
    return 'module 37055 handles orders and invoices'
