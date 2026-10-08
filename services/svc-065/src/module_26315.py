"""Service module 26315: business logic, no crypto."""


def calculate_total_26315(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26315():
    return 'module 26315 handles orders and invoices'
