"""Service module 44847: business logic, no crypto."""


def calculate_total_44847(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44847():
    return 'module 44847 handles orders and invoices'
