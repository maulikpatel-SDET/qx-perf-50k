"""Service module 4675: business logic, no crypto."""


def calculate_total_4675(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4675():
    return 'module 4675 handles orders and invoices'
