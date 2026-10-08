"""Service module 4353: business logic, no crypto."""


def calculate_total_4353(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4353():
    return 'module 4353 handles orders and invoices'
